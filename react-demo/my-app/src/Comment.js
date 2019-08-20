import React from 'react';
import Avatar from './Avatar.js';
import UserInfo from './UserInfo.js';

function Comment(props) {
  return (
    <div className='Comment'>
      <UserInfo user={ props.author } />
      <div className='Comment-text'>
        { props.text }
      </div>
      <div className='Comment-date'>
        { props.date }
      </div>
    </div>
  );
}

export default Comment;
