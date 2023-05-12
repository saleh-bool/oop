import React from 'react'
import {render} from '@testing-library/react'
import {AuthContextProvider} from './context/AuthContext'


const customRender = (ui, options) =>
  render(ui, {wrapper: AuthContextProvider, ...options})

// re-export everything
export * from '@testing-library/react'

// override render method
export {customRender as render}