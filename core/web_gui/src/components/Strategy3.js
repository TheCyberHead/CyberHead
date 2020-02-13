import React from 'react';

class Strategies extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('2')
	}

	render(){
		return(
			<React.Fragment>
				<h1>Strategy3</h1>
			</React.Fragment>
		)
	}
}

export default Strategies;
