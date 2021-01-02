import { ChildProcessWithoutNullStreams, spawn } from 'child_process'
import { Action, Speed } from '../enums'

export default class Motor {
    #scriptName: string
    #process: ChildProcessWithoutNullStreams | undefined

    constructor(scriptName: string) {
        this.#scriptName = scriptName
    }

    start() {
        if (typeof this.#process !== 'undefined') return
        this.#process = spawn('python', [`src/scripts/${this.#scriptName}.py`])
        console.log(`Feeder script started with PID ${this.#process.pid}`)
    }

    private sendCommand(command: string) {
        this.#process?.stdin.write(command + '\n')
    }

    stop() {
        this.sendCommand(Action.STOP)
        this.#process?.kill()
        this.#process = undefined
    }

    changeSpeed(speed: Speed) {
        this.sendCommand(speed)
    }
}