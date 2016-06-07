import React  from 'react';
import ReactDOM from 'react-dom';
class App extends React.Component {
	constructor() {
		super();
		this.state = {
			txt: 'this is the state txt',
			red: 0,
			blue: 0,
			green: 0
		}
	}
	update(e) {
		this.setState({
			red: ReactDOM.findDOMNode(this.refs.red).value,
			blue: ReactDOM.findDOMNode(this.refs.blue).value,
			green: ReactDOM.findDOMNode(this.refs.green).value,
		})
	}
	render(){
		return (
			<div>
				<Slider ref="red" update={this.update.bind(this)} />
				{this.state.red}
				<br />
				<Slider ref="blue" update={this.update.bind(this)} />
				{this.state.blue}
				<br />
				<Slider ref="green" update={this.update.bind(this)} />
				{this.state.green}
				<br />
			</div>
		) 
	}
}

class Slider extends React.Component {
	render() {
		return (
			<input type="range"
				min="0"
				max="255"
				onChange={this.props.update} />
		)
	}
}

App.propTypes = {
	txt: React.PropTypes.string.isRequired,
	number: React.PropTypes.number
}

App.defaultProps = {
	txt: 'this is the default text',
}

export default App;