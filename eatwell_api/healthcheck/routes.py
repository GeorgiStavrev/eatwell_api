from eatwell_api.healthcheck.views import HealthCheckView


def register_routes(app):
    app.router.add_route('*', '/healthcheck/', HealthCheckView)
    app.router.add_route('*', '/healthcheck', HealthCheckView)
