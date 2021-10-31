import React, { Component } from 'react'
import { render } from "react-dom"
import HomePage from "./HomePage"
export default class App extends Component {
    render() {
        return (
            <HomePage/>
        )
    }
}

render(<App/>,document.getElementById("app"))