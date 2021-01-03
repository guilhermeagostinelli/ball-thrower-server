# ball-thrower-server
RESTful API for controlling a table tennis ball thrower robot.

The robot consists of two motors: a feeder and a shooter. Each one is controlled by a separate python script that runs on a Raspberry Pi.

The shooter is a DC motor responsible for throwing the ball. The speed of the shooter determines the amount of spin generated in the ball.

The feeder consists of a stepper motor to which the feeder plate is attached. Its speed dictates how fast the ball reaches the shooter, thus determining the interval between each throw.

## Prerequisites
1. Make sure you have [npm](https://www.npmjs.com/get-npm) installed.
2. Download the project dependencies using `npm install`

## Getting Started
These instructions will get you a copy of the project up and running on your Raspberry Pi.

### Building
Just run `npm run build`

After the process, the files will be moved from the source (`src`) folder to the distribution (`dist`) folder and you should have a production-ready version of this project.

### Running
To start the HTTP server on port 3000, run `npm start`

## Available endpoints

### Status

To check if the server is up and running, send a GET request to /status

The server will respond with a 200 (OK) status in case it is running.

### Feeder

- To start the feeder motor, send a GET request to /feeder/start
- To change the speed of the feeder motor, send a GET request to /feeder/change-speed/SPEED where SPEED is one of the following:
    - `l` (low speed)
    - `m` (medium speed)
    - `h` (high speed)
- To stop the feeder motor, send a GET request to /feeder/stop

### Shooter

- To start the shooter motor, send a GET request to /shooter/start
- To change the speed of the shooter motor, send a GET request to /shooter/change-speed/SPEED where SPEED is one of the following:
    - `l` (low speed)
    - `m` (medium speed)
    - `h` (high speed)
- To stop the shooter motor, send a GET request to /shooter/stop

## Android/iOS App
On [this other repository](https://github.com/guilhermeagostinelli/ball-thrower-app) you can find the source code for an app that interacts with the aforementioned API.

## Contributing

Feel free to contribute with corrections, optimizations, etc. There are no strict guidelines on how one should contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.