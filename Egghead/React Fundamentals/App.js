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
				<input 
					type="text" 
					onChange={this.update.bind(this)} />
				<h1>{this.state.txt}</h1>
			</div>
			
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