import React from 'react';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);

    this.handleUserInput = this.handleUserInput.bind(this);
    this.handleCheckboxChange = this.handleCheckboxChange.bind(this);
  }

  handleUserInput(e) {
    this.props.handleUserInput(e.target.value);
  }

  handleCheckboxChange(e) {
    this.props.handleCheckboxChange(e.target.checked);
  }

  render() {
    const userInput = this.props.userInput;
    const isCheckedOnly = this.props.isCheckedOnly;

    return (
      <div className='search-bar'>
        <input
          type='text'
          value={userInput}
          onChange={this.handleUserInput}
          placeholder='Search...'
        />
        <span>
          <input
            type='checkbox'
            checked={isCheckedOnly}
            onChange={this.handleCheckboxChange}
          />
          <label>Only show products in stock</label>
        </span>
      </div>
    );
  }
}

export default SearchBar;
