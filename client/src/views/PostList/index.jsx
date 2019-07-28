import { Query } from "react-apollo";

import gql from "graphql-tag";
import React from "react";
import exitIntent from 'exit-intent'
import { Divider, Modal, Button, Image, Header } from 'semantic-ui-react'
import { slide as Menu } from 'react-burger-menu'
import { QueryOpts, ChildDataProps, withApollo, graphql, compose } from 'react-apollo'

const categoryQuery = gql`
  query search($brand: String!) {
    search(brand: $brand) {
      id
      heroUrl
      logoUrl
      ctaText
      singleLiner
    }
  }
`

const queryString = require('query-string');

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
            eventThrottle: 3000,
            onExitIntent: () => {
                this.setState({visible: true})
            }
        })
    }

    render = () => {
        const {data} = this.props

        return (
            <>
            <Menu right isOpen={this.state.visible} noOverlay customBurgerIcon={ false } width={400}>
            {data.search && data.search.map((brand,i) => (
                <>
                <Image src={brand.heroUrl}/>
                <br/>
                <Image src={brand.logoUrl}/>
                <br/>
                <p>{brand.singleLiner}</p>
                <a target="_blank" href={brand.url}><Button>{brand.ctaText}</Button></a>
                <Divider/>
                </>
                )
            )}
                </Menu>
            </>
        )
    }
}

const queryOptions = {
    options: props => ({
        variables: {
            brand: queryString.parse(props.location.search).brand
        },
    }),
}

export default graphql(categoryQuery, queryOptions)(ReportObstruction)
