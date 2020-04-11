import React from 'react';
import AceEditor from "react-ace";
import {loadStrategiesEditor, getStrategyEdit} from '../actions/strategies'
import 'ace-builds/src-noconflict/mode-python'
import 'ace-builds/src-noconflict/snippets/python'
import 'ace-builds/src-noconflict/theme-monokai'

class CodeEditor extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true,
			strategiesEdit: [],
			currentName: '',
			currentCode: ''
		}
		this.loadStrategies = this.loadStrategies.bind(this)
		this.loadStrategy = this.loadStrategy.bind(this)
	}

	loadStrategies(){
		this.setState({load: false})
		loadStrategiesEditor()
			.then(response => {
				if (response['strategies'].length > 0) {
					this.setState({currentName: response['strategies'][0]})
					getStrategyEdit(response['strategies'][0])
						.then(response => this.setState({currentCode: response['strategy_code']}))
				}
				this.setState({strategiesEdit: response['strategies'], load: true})
			})

	}

	loadStrategy(ev){
		this.setState({load: false})
		getStrategyEdit(ev.target.dataset.strategy)
			.then(response => this.setState({currentCode:response['strategy_code'], load: true}))
	}

	componentDidMount(){
		this.loadStrategies()
		this.props.updateKey('7')
	}

	render(){
		return(
			<React.Fragment>
			<h2 style={{ color: '#ffffff'}}>Edit Strategies</h2>
			{this.state.load &&
			<div className="editor-box">
			<AceEditor
			  placeholder="Placeholder Text"
			  mode="python"
			  theme="monokai"
			  name="blah2"
			  onLoad={this.onLoad}
			  onChange={this.onChange}
			  fontSize={14}
			  showPrintMargin={true}
			  showGutter={true}
			  highlightActiveLine={true}
			  value={this.state.currentCode}
			  setOptions={{
			  enableBasicAutocompletion: false,
			  enableLiveAutocompletion: false,
			  enableSnippets: false,
			  showLineNumbers: true,
			  tabSize: 2,
			  }}/>
			 <div className="strategies_box">
			 	<p>Editor</p>
			 	<ul>
			 		{this.state.strategiesEdit.map(strategy => (
			 			<li key={strategy} data-strategy={strategy} onClick={this.loadStrategy}>{strategy}</li>
			 		))}
			 	</ul>
			 </div>
				</div>
				}
			</React.Fragment>
		)
	}
}

export default CodeEditor;