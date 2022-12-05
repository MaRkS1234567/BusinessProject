'use strict';


class App extends React.Component {
  render() {
    return (
      <h3 className="red">Hello mark</h3>
    );
  }
}

let domContainer = document.querySelector('#mainapp');
ReactDOM.render(<App />, domContainer);

// const domContainer = document.querySelector('#mainapp');
// const root = ReactDOM.createRoot(domContainer);
// root.render(App);