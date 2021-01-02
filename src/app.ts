import { ChildProcessWithoutNullStreams, spawn } from 'child_process'
import express from 'express'
import { Action, Speed } from './enums'
import { PORT } from './helper/constants'

const app = express()

let feederScript: ChildProcessWithoutNullStreams | undefined

function startFeeder() {
    if (typeof feederScript !== 'undefined') return
    feederScript = spawn('python', ['feeder.py'])
    console.log(`Feeder script started with PID ${feederScript.pid}`)
}

function sendCommandToFeeder(command: string) {
    feederScript?.stdin.write(command + '\n')
}

function stopFeeder() {
    sendCommandToFeeder(Action.STOP)
    feederScript?.kill()
    feederScript = undefined
}

function changeFeederSpeed(speed: Speed) {
    sendCommandToFeeder(speed)
}

app.get('/feeder/start', (req, res) => {
    startFeeder()
    res.sendStatus(200)
})

app.get('/feeder/change-speed/:speed', (req, res) => {
    changeFeederSpeed(<Speed>req.params['speed'])
    res.sendStatus(200)
})

app.get('/feeder/stop', (req, res) => {
    stopFeeder()
    res.sendStatus(200)
})

app.listen(PORT, () =>
    console.log(`server is listening on ${PORT}`)
)