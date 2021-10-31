import React, { Component } from 'react'
import { 
    Button,
    Grid,
    Typography,
    TextField,
} from "@material-ui/core";
import { Link } from "react-router-dom";


export default class RoomJoinPage extends Component {
    state={
        roomCode:"",
        error:"",
    }
    roomButtomPress=()=>{
        const requestOptins={
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                code:this.state.roomCode
            })
        }
        fetch("/api/join-room",requestOptins)
            .then(res=>{
                if (res.ok){
                    this.props.history.push("/room/"+this.state.roomCode);
                }else{
                    res.json()
                        .then(data=>{
                            this.setState({
                                error:data.message
                            })
                        })
                }
            })
    }        
    render() {
        return (
            <Grid container alignContent='center' alignItems="center" spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography variant='h4' component='h4'>
                        Join a Room
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField 
                        error={this.state.error}
                        label="Code"
                        placeholder="Enter Room Code"
                        type="text"                       
                        value={this.state.roomCode}
                        helperText={this.state.error}
                        variant="outlined"
                        onChange={e=>{this.setState({roomCode:e.target.value})}}
                    />
                </Grid>
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="primary" onClick={this.roomButtomPress}>
                        Enter Room
                    </Button>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="secondary" to="/" component={Link}>
                        Back
                    </Button>
                </Grid>
            </Grid>
        )
    }
}
