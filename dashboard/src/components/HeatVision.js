import React from 'react';

class HeatVision extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('3')
	}

	render(){
		return(
			<React.Fragment>
				<h1>HeatVision</h1>
			</React.Fragment>
		)
	}
}

export default HeatVision;