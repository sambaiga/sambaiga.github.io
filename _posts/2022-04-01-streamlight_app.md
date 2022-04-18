---
layout: post
title: Going Beyond Train/test with Streamlit
subtitle: Creating data app with Streamlit
subsubtitle: Creating data app with streamlight.
date: 2022-04-01
description: This post introduce energy-based model 
author: Anthony Faustine 
image: ebm.jpg
---

## Introduction
The common practice for applying machine learning to real-world problems is to build a machine learning model using a training set and evaluate its generalisation ability on the test set. While this practice is acceptable for ML researchers, it does not offer adequate room for other users to test and interact with the developed ML algorithm. Allowing end-users to interact with the developed ML algorithms generates interest and makes the end-user part of the ML development and evaluation. Nevertheless, building such an interactive demo has not been straightforward due to the software engineering efforts required to make that happen. Several tools such as [Streamlit](https://streamlit.io/), [Dash](https://plotly.com/dash/),  [gradio](https://gradio.app/) and [panel ](https://panel.holoviz.org/) in the Python dashboarding ecosystem have been realised to simplify this process. This post will focus on [Streamlit](https://streamlit.io/). 

## Streamlit
[Streamlit](https://streamlit.io/) is an open-source Python library that makes it easy to create and share data apps for machine learning and data science.  Streamlit is compatible with the majority of python machine learning libraries.  Consequently, it makes it easy to create data apps reusing the same python code used in developing the ML algorithm.  Thus it makes it easy to work on the interactive loop of coding and viewing results in the web app.  The streamlit API treats the widget as variables, making it easy to build an interactive app without writing HTML, CSS, JavaScript, etc.  Deploying and sharing the data apps is also straightforward with With Streamlit Cloud.  With  streamlit cloud you can share, manage, and collaborate directly from Streamlit.

## Building Streamlit app for FPSe2Q forecasting model
In this post, I will use streamlit to create a demo of our recent publication [FPSeq2Q: Full Distributional Net-Load Forecasting with Parameterized Quantile Regression](https://ieeexplore.ieee.org/document/9701598). The demo is created using   [Hierarchical Substation Load demand dataset (HLD)]() dataset, which consists of three-phases power measurements and meteorological data such as radiation and air temperature. The data was collected from 24 secondary substations nodes with an average power of 81 kW in Rolle (Switzerland).   The task is to provide a probabilistic one-day ahead forecast of aggregated average power,  which is the sum of all the nodes.

### Create streamlit app
The first step is installing streamlit as follows ``  pip install streamlit``.  To test if streamlit is installed successfully, run this command on terminal ``$ streamlit hello ``. After creating the app, launching it is as easy as running ``streamlit run app.py``.

To create streamlit app 
1. First configures the default settings of the page using ``st.set_page_config(page_title=None, page_icon=None, layout="centered")``. For example 

```
st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)
```
2. Define navigation bar for the app. There is no standard streamlit widget for this, yet there exist third part widget that could be used for this purpose. [Hydralit Components](https://github.com/TangleSpace/hydralit_components)  is a popular package of streamlit components that provide the navbar widget. Install this package ``pip install -U hydralit_components `` then define the navigation bar of the app as follows:

```python
menu_data = [
    {'icon':"far fa-line-chart", 'label':"Data Analysis"},
    {'icon':"far fa-info-circle", 'label':"Forecasting"}, 
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home'
)
```






