import React from 'react';

class Strategy extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true,
			strategyName: ''
		}
	}

	componentDidMount(){
		console.log(this.props.match)
		// const { match: { params } } = this.props;
		// this.setState({strategyName: params.strategy_name})
	}

	render(){
		return(
			<React.Fragment>
				<h1>Strategy Dynamic</h1>
			</React.Fragment>
		)
	}
}

export default Strategy;