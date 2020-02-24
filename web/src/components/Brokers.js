import React from 'react';
import alpaca from '../alpaca.png'
import ameritrade from '../ameritrade.svg'
import coinbase from '../coinbase.svg'

class Brokers extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('6')
	}

	render(){
		return(
			<div>
				<h1 style={{ color: '#ffffff'}}>Brokers</h1>
				<div className="submit_broker">
					<div className="broker_images">
						<img src={alpaca} />
						<img src={ameritrade} />
						<img src={coinbase} />
					</div>
				</div>
			</div>
		)
	}
}

export default Brokers;