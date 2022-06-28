"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_process_viewset():
    import routes.processes as ExtendViewSet
    return ExtendViewSet.ProcessViewSet

def get_user_viewset():
    import seed.routes.users as SeedViewSet
    return SeedViewSet.UserViewSet

def get_file_view():
    import seed.routes.files as SeedView
    return SeedView.FileView

ProcessViewSet = get_process_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()