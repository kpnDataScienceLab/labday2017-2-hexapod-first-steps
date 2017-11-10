import java.io._
import java.util._
import gnu.io._

object Commander {
  var portList: Enumeration[String] = _
  var portId: CommPortIdentifier = _
  var serialPort: SerialPort = _
  var outputStream: OutputStream = _
  var right_V = 128 // Vertical position of the right joystick. 0 = All the way down, 127 = centered, 255 = all the way up
  var right_H = 128 // Horizontal position of the right joystick. 0 = All the way left, 127 = centered, 255 = all the way right
  var left_H = 128 // Vertical position of the right joystick. 0 = All the way down, 127 = centered, 255 = all the way up
  var left_V = 255 // Horizontal position of the right joystick. 0 = All the way left, 127 = centered, 255 = all the way right
  var allButtons = 1

  def delayMs(ms: Int): Unit = {
    val time = System.currentTimeMillis()
    while ( {System.currentTimeMillis() - time < ms}) {}
  }

  def sendCommand(): Unit = {
    if (serialPort != null) {
      outputStream.write(0xff) //header
      outputStream.write(right_V.toByte) //right vertical joystick
      outputStream.write(right_H.toByte) //right horizontal joystick
      outputStream.write(left_V.toByte) //left vertical joystick
      outputStream.write(left_H.toByte) //left horizontal joystick
      outputStream.write(allButtons) //single byte holds all the button data
      outputStream.write(0.toByte) //0 char
      outputStream.write((255 - (right_V + right_H + left_V + left_H + allButtons) % 256).toByte) //checksum
      delayMs(33) //delay 33ms for 30hz
    }
  }

  def main(args: Array[String]) {
    val portList = CommPortIdentifier.getPortIdentifiers()
    while (portList.hasMoreElements()) {
      portId = portList.nextElement().asInstanceOf[CommPortIdentifier]
      println(s"portName ${portId.getName()}")
      if (portId.getPortType() == CommPortIdentifier.PORT_SERIAL) {
        if (portId.getName().equals("/dev/ttyUSB0")) {
          try {
            serialPort = portId.open("Test", 2000).asInstanceOf[SerialPort]
          } catch {
            case piue: PortInUseException => piue.printStackTrace()
          }
          try {
            outputStream = serialPort.getOutputStream()
          } catch {
            case ioe: IOException => ioe.printStackTrace()
          }
          try {
            serialPort.setSerialPortParams(38400, SerialPort.DATABITS_8, SerialPort.STOPBITS_1, SerialPort.PARITY_NONE)
          } catch {
            case ue: UnsupportedCommOperationException => ue.printStackTrace()
          }
          try {
            sendCommand()
            //            outputStream.write(messageString.getBytes())
            //            println(messageString)
            //            outputStream.close()
            //            serialPort.close()
          } catch {
            case ioe: IOException => ioe.printStackTrace()
          }
        }
      }
    }
  }
}