import React from 'react';
import logo from './logo.svg';
import './App.css';
import Clock from './Clock.js';
import Toggle from './Toggle.js';
import FilterableProductTable from './FilterableProductTable.js';
import Timer from './Timer.js';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isToggleOn: true
    }
    this.handleToggle = this.handleToggle.bind(this);
  }

  handleToggle() {
    this.setState(state => ({
      isToggleOn: !state.isToggleOn
    }));
  }

  render() {
    return (
      <div className="App">
        <Clock isToggleOn={this.state.isToggleOn} />
        <Clock isToggleOn={this.state.isToggleOn} />
        <Clock isToggleOn={this.state.isToggleOn} />
        <Toggle isToggleOn={this.state.isToggleOn} handleToggle={this.handleToggle} />
        <FilterableProductTable />
        <Timer />
      </div>
    );
  }
}

export default App;
