# ball-thrower-server
RESTful API for controlling a ball thrower robot.

A python script is used for controlling a stepper motor to which the ball feeder plate is attached.

## Prerequisites
1. Make sure you have [npm](https://www.npmjs.com/get-npm) installed.
2. Download the project dependencies using `npm install`

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development purposes. See Building section for notes on how to deploy the project on a live system.

### Running
To create a simple HTTP server on port 3000, run `npm start`

### Starting the feeder
To start the feeder motor, send a GET request to http://localhost:3000/feeder/start

### Changing the feeder speed
To change the speed of the feeder motor, send a GET request to http://localhost:3000/feeder/change-speed/SPEED where SPEED is one of the following:
- `l` (low speed)
- `m` (medium speed)
- `h` (high speed)

For instance, sending a GET request to http://localhost:3000/feeder/change-speed/h will change the feeder to high speed.

### Stopping the feeder
To stop the feeder motor, send a GET request to http://localhost:3000/feeder/stop

## Building
Just run
    `npm run build`

After the process, the files will be moved from the source (`src`) folder to the distribution (`dist`) folder and you should have a production-ready version of this project.

## Contributing

Feel free to contribute with corrections, optimizations, etc. There are no strict guidelines on how one should contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.