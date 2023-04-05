from django.urls import path

from . import views

urlpatterns = [
    path('vessel_managet_net_sample/ships/', views.ShipList.as_view()),
    path('vessel_managet_net_sample/ships-overview/', views.ShipOverviewList.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/', views.ShipDetail.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/specs/',
         views.ShipSpecsCreate.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/voyages/',
         views.ShipVoyageList.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/latest-voyage/',
         views.LatestVoyageDetailByShip.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/reports/',
         views.ShipReportsList.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/latest-report/',
         views.LatestReportDetailByShip.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/legs/', views.ShipLegsList.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/latest-details/',
         views.ReportPrefillView.as_view()),
    path('vessel_managet_net_sample/voyages/', views.VoyageList.as_view()),
    path('vessel_managet_net_sample/voyages/<uuid:uuid>/', views.VoyageDetail.as_view()),
    path('vessel_managet_net_sample/voyages/<uuid:uuid>/reports/',
         views.VoyageReportsList.as_view()),
    path('vessel_managet_net_sample/reports/', views.ReportsList.as_view()),
    path('vessel_managet_net_sample/reports/<uuid:uuid>/', views.ReportDetail.as_view()),
    path('vessel_managet_net_sample/ships/<int:imo_reg>/stats/',
         views.WeeklyStatsList.as_view()),
    path('vessel_managet_net_sample/user/', views.UserProfileView.as_view()),
]
