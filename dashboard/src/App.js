import React from 'react';
import SideBar from './components/SideBar'
import './App.css';

class App extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			collapsed: false
			}
		}
		render(){
			return (
					<SideBar />
				)
		}
}

export default App;
