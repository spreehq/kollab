import { Query } from "react-apollo";

import gql from "graphql-tag";
import React from "react";
import exitIntent from 'exit-intent'
import { Modal, Button, Image, Header } from 'semantic-ui-react'
import { slide as Menu } from 'react-burger-menu'



class ReportObstruction extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            visible: false
        }
    }

    componentDidMount = () => {
        const removeExitIntent = exitIntent({
            threshold: 50,
            maxDisplays: 2,
            eventThrottle: 100,
            onExitIntent: () => {
                this.setState({visible: true})
            }
        })
    }

    render = () => {
        return (
            <>
            <Menu right isOpen={this.state.visible} noOverlay customBurgerIcon={ false }>
            <h2>Whoa whoa whoa</h2>
            <p>blah</p>
            </Menu>
            </>
        )
    }
}

export default ReportObstruction
