import React from 'react';
import ProductCategoryRow from './ProductCategoryRow.js';
import ProductRow from './ProductRow.js';

class ProductTable extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const userInput = this.props.userInput;
    const inStockOnly = this.props.inStockOnly;
    const rows = [];
    let lastCategory = null;

    this.props.products.forEach((product) => {
      if (inStockOnly && !product.stocked) {
        return;
      }

      if (product.name.toLowerCase().indexOf(userInput) === -1) {
        return;
      }

      if (product.category !== lastCategory) {
        rows.push(
          <ProductCategoryRow category={product.category} key={product.category} />
        );
      }

      rows.push(
        <ProductRow name={product.name} price={product.price} key={product.name} />
      );
      
      lastCategory = product.category;
    });

    return (
      <table className='product-table'>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    );
  }
}

export default ProductTable;
