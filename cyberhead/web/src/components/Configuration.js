import React from 'react';

class Configuration extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('4')
	}

	render(){
		return(
			<React.Fragment>
				<h1>Configuration</h1>
			</React.Fragment>
		)
	}
}

export default Configuration;