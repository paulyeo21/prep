import React from 'react';
import SearchBar from './SearchBar.js';
import ProductTable from './ProductTable.js';
import data from './data.js'

class FilterableProductTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userInput: '',
      inStockOnly: false
    };

    this.handleUserInput = this.handleUserInput.bind(this);
    this.handleCheckboxChange = this.handleCheckboxChange.bind(this);
  }

  handleUserInput(userInput) {
    this.setState({
      userInput: userInput
    })
  }

  handleCheckboxChange(inStockOnly) {
    this.setState({
      inStockOnly: inStockOnly
    });
  }

  render() {
    return (
      <div className='filterable-product-table'>
        <SearchBar
          handleUserInput={this.handleUserInput}
          handleCheckboxChange={this.handleCheckboxChange}
          userInput={this.state.userInput}
          inStockOnly={this.state.inStockOnly}
        />
        <ProductTable
          products={data}
          userInput={this.state.userInput}
          inStockOnly={this.state.inStockOnly}
        />
      </div>
    );
  }
}

export default FilterableProductTable;
