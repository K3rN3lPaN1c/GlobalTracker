import requests
import plotly.graph_objs as go
from django.shortcuts import render
from django.http import JsonResponse


def global_temperature(request):
    # Get temperature data from the API
    api_url = 'https://global-warming.org/api/temperature-api'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        temperature_data = data['result']

        # Extract the x and y data from the input data
        x = [float(datum["time"]) for datum in temperature_data]
        y1 = [float(datum["station"]) for datum in temperature_data]
        y2 = [float(datum["land"]) for datum in temperature_data]

        # Create a new line chart using Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y1, name="Station", mode="lines"))
        fig.add_trace(go.Scatter(x=x, y=y2, name="Land", mode="lines"))

        # Set the chart title and axis labels
        fig.update_layout(title="Global Temperature Data", xaxis_title="Time", yaxis_title="Temperature")

        # Enable hover information on the chart
        fig.update_layout(hovermode="x")

        # Set the plotly template to a dark theme
        fig.update_layout(template="plotly_dark")

        # Convert the Plotly chart to HTML and pass it to the template context
        plot_div = fig.to_html(full_html=False)

        # Render the graph template with the Plotly chart
        return render(request, 'graph.html', {'plot_div': plot_div})

    else:
        return JsonResponse({'error': 'Failed to retrieve temperature data.'})
