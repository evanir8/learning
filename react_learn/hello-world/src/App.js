
import ReactDOM from 'react-dom';
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Bemvindo ao React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

var Card = React.createClass({

  getInitialState: function(){
    return {
      logo : "logo-labs.png",
      text : "Nosso primeiro aplicativo com React.js..."
    }
  },

  changeCard : function(){
    this.setState({
      logo : "logo-polvo.png",
      text : "You take the red pill, you stay in Wonderland, and ...."
    })
  },

  render : function(){
    var img = "./img/"+this.state.logo;
    return (
      <article className="Card">
        <img src={logo} className="App-logo" alt="logo"/>
        <p>{this.state.text}</p>
        <button onClick={this.changeCard}>Execute..</button>
      </article>
    )
  }
})
ReactDOM.render(<Card/>, document.getElementById('card'))

function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
export default App;
