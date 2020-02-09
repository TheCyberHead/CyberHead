import React from 'react';

class DataSets extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('5')
	}

	render(){
		return(
			<React.Fragment>
				<h1>DataSets</h1>
			</React.Fragment>
		)
	}
}

export default DataSets;