# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.1] - 2021-01-03
### Fixed
- Prepared both feeder.py and shooter.py scripts to print the stack trace of exceptions.
- Adjusted both feeder.py and shooter.py scripts to reset the GPIO pins no matter what happens in the execution flow.
- Changed the feeder script to use a single phase stepping mode instead of a half stepping mode sequence to control the stepper motor.
- Adjusted the speed of the feeder.
- Fixed the usage of the relative filepath when spawning a python process.
- The output from the python scripts is now logged into the server console.

## [1.2.0] - 2021-01-02
### Added
- Endpoint that the client can use to verify if the server is up and running.

## [1.1.0] - 2021-01-02
### Added
- Endpoint for starting the ball shooter motor.
- Endpoint for stopping the ball shooter motor.
- Endpoint for changing the speed of the ball shooter motor.

## [1.0.0] - 2021-01-01
### Added
- Endpoint for starting the ball feeder motor.
- Endpoint for stopping the ball feeder motor.
- Endpoint for changing the speed of the ball feeder motor.

[Unreleased]: https://github.com/guilhermeagostinelli/ball-thrower-server/compare/v1.2.1...develop
[1.2.1]: https://github.com/guilhermeagostinelli/ball-thrower-server/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/guilhermeagostinelli/ball-thrower-server/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/guilhermeagostinelli/ball-thrower-server/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/guilhermeagostinelli/ball-thrower-server/releases/tag/v1.0.0