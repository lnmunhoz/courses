import React  from 'react';
class App extends React.Component {
	constructor() {
		super();
		this.state = {
			txt: 'this is the state txt'
		}
	}
	update(e) {
		this.setState({txt: e.target.value})
	}
	render(){
		return (
			<div>
				<Widget txt={this.state.txt} update={this.update.bind(this)} />
				<Widget txt={this.state.txt} update={this.update.bind(this)} />
				<Widget txt={this.state.txt} update={this.update.bind(this)} />
				<Widget txt={this.state.txt} update={this.update.bind(this)} />		
			</div>
		) 
	}
}

const Widget = (props) => {
		return (
			<div>
				<input 
					type="text" 
					onChange={props.update} />
				<h1>{props.txt}</h1>
			</div>
		) 
}

App.propTypes = {
	txt: React.PropTypes.string.isRequired,
	number: React.PropTypes.number
}

App.defaultProps = {
	txt: 'this is the default text',
}

export default App;