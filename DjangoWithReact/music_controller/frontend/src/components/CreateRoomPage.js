import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import { Link } from "react-router-dom";

export default class CreateRoomPage extends Component {
    defaultVotes = 2;
    state={
        voteToSkip:this.defaultVotes,
        guestCanPause:true,
    }
    constructor(props){
        super(props);
        this.handleGuestCanPauseChange = this.handleGuestCanPauseChange.bind(this);
        this.handleVotesChange = this.handleVotesChange.bind(this);
        this.handleRoomButtonPressed = this.handleRoomButtonPressed.bind(this);
    }
    handleVotesChange (e) {
        this.setState({
            voteToSkip:e.target.value
        });
    }
    handleGuestCanPauseChange(e){
        this.setState({
            guestCanPause:e.target.value==="true"
        });
    }
    handleRoomButtonPressed(){
        const requestOptins={
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                guest_can_pause:this.state.guestCanPause,
                vote_to_skip:this.state.voteToSkip
            })
        }
        fetch("/api/create-room",requestOptins)
            .then(res=>{
                res.json()  
                    .then(data=>{
                        this.props.history.push("/room/"+data.code);
                    })
            })
    }
    render() {
        return (
            <Grid container alignContent='center' spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        Create a Room
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl component="fieldset">
                        <FormHelperText>
                            <div align="center"> Guest Control to Playback State</div>
                        </FormHelperText>
                        <RadioGroup row defaultValue="true" onChange={this.handleGuestCanPauseChange}>
                            <FormControlLabel 
                                control={<Radio color="primary"/>}
                                value="true"
                                label="Play/Pause"
                                labelPlacement="bottom"
                                />
                            <FormControlLabel 
                                control={<Radio color="secondary"/>}
                                value="false"
                                label="No Control"
                                labelPlacement="bottom"
                                />
                        </RadioGroup>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <TextField 
                            required={true}
                            defaultValue={this.defaultVotes}
                            type="number"
                            onChange={this.handleVotesChange}
                            inputProps={{
                                min:1,
                                style:{
                                    textAlign:"center"
                                }
                            }}
                        />
                        <FormHelperText>
                            <div align="center"> Votes Required to Skip Song</div>
                        </FormHelperText>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="primary" onClick={this.handleRoomButtonPressed}>Create a Room</Button>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="secondary" to="/" component={Link}>Back</Button>
                </Grid>
            </Grid>
        )
    }
}
