import React from 'react';

class Toggle extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <button onClick={this.props.handleToggle}>
        {this.props.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

export default Toggle;
