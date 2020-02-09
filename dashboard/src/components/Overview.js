import React from 'react';

class Overview extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('1')
	}

	render(){
		return(
			<React.Fragment>
				<h1>Overview</h1>
			</React.Fragment>
		)
	}
}

export default Overview;