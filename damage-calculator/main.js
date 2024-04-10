import express from 'express'
import body_parser from 'body-parser'
import {calculate, Generations, Pokemon, Move, Field, Side} from '@smogon/calc'
import dex from 'pokemon-showdown'


const {Dex} = dex
const app = express()

app.use(body_parser.urlencoded({ extended: false }))
app.use(body_parser.json())


app.post("/calc-damage",
    function (req, res) {
        console.log(req.body)
        const result = calculate(
            req.body.gen,
            new Pokemon(req.body.gen, req.body.pkm1.name, req.body.pkm1.fields),
            new Pokemon(req.body.gen, req.body.pkm2.name, req.body.pkm2.fields),
            new Move(req.body.gen, req.body.move),
            new Field(req.body.field)
        )
        console.log(result)
        res.setHeader('Content-Type', 'application/json')
        res.send(JSON.stringify(result))
    })


app.get("/test-calc",
    function (req, res) {
        const result = calculate(
            8, 
            new Pokemon(8, 'Charizard', {
                'item': 'Choice Band',
                'ability': 'Drought',
                'ivs': {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31},
                'evs': {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31},
                'nature': 'Bold',
                'status': '',
                'boosts': {'hp': 0, 'atk': 1, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0},
            }),
            new Pokemon(8, 'Charizard', {
                'item': 'Choice Band',
                'ability': 'Drought',
                'ivs': {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31},
                'evs': {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31},
                'nature': 'Bold',
                'status': '',
                'boosts': {'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0},
            }),
            new Move(8, 'Flare Blitz'),
            new Field({weather: 'Rain'})
        )
        console.log(result)
        res.setHeader('Content-Type', 'application/json')
        res.send(JSON.stringify(result))
    }
)


app.get('/test-dex',
    function (req, res) {
        const move = Dex.mod('gen8').moves.get('Mortal Spin')
        res.setHeader('Content-Type', 'application/json')
        res.send(JSON.stringify(move))
    }
)


app.listen(3000, function () {
    console.log(
        "server is running on port 3000"
    )
})

