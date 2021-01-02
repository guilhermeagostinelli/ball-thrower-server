import express from 'express'
import { Speed } from './enums'
import { PORT } from './helper/constants'
import Motor from './helper/Motor'

const app = express()

const feeder = new Motor('feeder')
const shooter = new Motor('shooter')

app.get('/feeder/start', (req, res) => {
    feeder.start()
    res.sendStatus(200)
})
app.get('/feeder/change-speed/:speed', (req, res) => {
    feeder.changeSpeed(<Speed>req.params['speed'])
    res.sendStatus(200)
})
app.get('/feeder/stop', (req, res) => {
    feeder.stop()
    res.sendStatus(200)
})

app.get('/shooter/start', (req, res) => {
    shooter.start()
    res.sendStatus(200)
})
app.get('/shooter/change-speed/:speed', (req, res) => {
    shooter.changeSpeed(<Speed>req.params['speed'])
    res.sendStatus(200)
})
app.get('/shooter/stop', (req, res) => {
    shooter.stop()
    res.sendStatus(200)
})

app.listen(PORT, () =>
    console.log(`server is listening on ${PORT}`)
)