import React from 'react';

class Timer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      time: 0,
      start: 0,
      hasStarted: false
    }

    this.startTimer = this.startTimer.bind(this);
    this.stopTimer = this.stopTimer.bind(this);
    this.resetTimer = this.resetTimer.bind(this);
  }

  startTimer() {
    this.setState(state => ({
      time: state.time,
      start: Date.now() - state.time,
      hasStarted: true
    }));
    this.timer = setInterval(() => this.setState(state => ({
      time: Date.now() - state.start
    })), 1000);
    console.log('start');
  }

  stopTimer() {
    this.setState({
      hasStarted: false
    });
    clearInterval(this.timer);
    console.log('stop');
  }

  resetTimer() {
    this.setState({
      time: 0,
      hasStarted: false
    });
    console.log('reset');
  }

  render() {
    const startButton = (this.state.time === 0) ? <button onClick={this.startTimer}>start</button> : null
    const stopButton = (this.state.hasStarted) ? <button onClick={this.stopTimer}>stop</button> : null
    const resumeButton = (this.state.time !== 0 && !this.state.hasStarted) ? <button onClick={this.startTimer}>resume</button> : null
    const resetButton = (this.state.time !== 0 && !this.state.hasStarted) ? <button onClick={this.resetTimer}>reset</button> : null

    return (
      <div>
        <h3>timer: {this.state.time}</h3>
        {startButton}
        {stopButton}
        {resumeButton}
        {resetButton}
      </div>
    );
  }
}

export default Timer;
