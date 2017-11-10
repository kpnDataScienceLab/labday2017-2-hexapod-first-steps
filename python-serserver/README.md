# connect via http to hexapod


Once connected:

    curl -X POST --data-binary @test.json http://euclid:9100

# Data structure

The data structure maps the remote controls actuator values: right/left, vertical/horizontal and buttons.
You send a json encoded version of the parameters to the endpoint, and the robot responds.

    {"rv":128, "rh":128, "lv":128, "lh":128, "b0":0, "b1":0, "b2":0, "b3":1, "b4":1, "b5":1, "b6":1, "b7":1}
