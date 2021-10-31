import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route,Link, Redirect } from "react-router-dom";
import RoomJoinPage from './RoomJoinPage'
import CreateRoomPage from './CreateRoomPage'
import Room from './Room'
import { 
    Button,
    Grid,
    Typography,
    ButtonGroup,
} from "@material-ui/core";

export default class HomePage extends Component {
    state={
        roomCode:null,
    }
    async componentDidMount(){
        const res = await fetch("api/user-in-room");
        const data = await res.json();
        this.setState({
            roomCode:data.code
        })
        console.log(data);

    }
    clearRoom=()=>{
        this.setState({
            roomCode:null
        })
    }
    renderHomePage=()=>{
        return (
            <Grid container alignContent='center' spacing={3}>
                <Grid item xs={12} align="center">
                    <Typography component="h3" variant="h3">
                        House Party
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <ButtonGroup variant="contained" color='primary'>
                        <Button color="primary" to="/join" component={Link}>
                            Join a Room
                        </Button>
                        <Button color="secondary" to="/create" component={Link}>
                            Create a Room
                        </Button>
                    </ButtonGroup>
                </Grid>
            </Grid>
        );
    }
    render() {
        return (
            <Router>
                <Switch>
                    <Route exact path="/" render={()=>{
                        return this.state.roomCode ? (<Redirect to={`room/${this.state.roomCode}`}/>): this.renderHomePage() 
                    }}/>
                    <Route path="/join" component={RoomJoinPage}/>
                    <Route path="/create" component={CreateRoomPage}/>
                    <Route path="/room/:roomCode" render={(props)=>{
                        return (<Room leaveRoomCallBack={this.clearRoom} {...props}/>)
                    }}/>
                </Switch>
            </Router>
        )
    }
}
