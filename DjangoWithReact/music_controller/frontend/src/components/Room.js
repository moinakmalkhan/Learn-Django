import React, { Component } from 'react'
import { 
    Button,
    Grid,
    Typography,
} from "@material-ui/core";
// import { Link } from "react-router-dom";


export default class Room extends Component {
    state={
        voteToSkip:2,
        guestCanPause:true,
        isHost:false,
    }
    constructor(props){
        super(props)
        this.roomCode=this.props.match.params.roomCode;
        // this.getRoom()
        console.log(this.props);
    }
    componentDidUpdate(){
        fetch("/api/get-room?code="+this.roomCode)
            .then(res=>{
                if (res.ok){
                    res.json()  
                        .then(data=>{
                            this.setState({
                                voteToSkip:data.vote_to_skip,
                                guestCanPause:data.guest_can_pause,
                                isHost:data.is_host
                            })
                        })
                }
                else{
                    this.setState({
                        voteToSkip:null,
                        guestCanPause:null,
                        isHost:null
                    })
                }
            })
    }
    leaveRoom=()=>{
        
        fetch("/api/leave-room")
            .then(res=>{
                this.props.leaveRoomCallBack();
                console.log("deleted");
                this.props.histroy.push("/");

            })
    }
    render() {
        return (
            
            <Grid container alignContent='center' spacing={3}>
                <Grid item xs={12} align="center">
                    <Typography component="h5" variant="h5">
                        Code: {this.roomCode}
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography component="h5" variant="h5">
                        Vote to skip: {this.state.voteToSkip}
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography component="h5" variant="h5">
                        Guest can pause: {this.state.guestCanPause===true?"Yes":"No"}
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography component="h5" variant="h5">
                        Is Host: {this.state.isHost===true?"Yes":"No"}
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="secondary" onClick={this.leaveRoom}>
                        Leave Room
                    </Button>                
                </Grid>
                <Grid item xs={12} align="center">
                </Grid>
            </Grid>
        )
    }
}

            // <div>
            //     <h1>Room code:{this.roomCode}</h1>
            //     <p>Vote: {this.state.voteToSkip}</p>
            //     <p>Guest can skip: {this.state.guestCanPause===true?"Yes":"No"}</p>
            //     <p>Is Host: {this.state.isHost===true?"Yes":"No"}</p>
            // </div>