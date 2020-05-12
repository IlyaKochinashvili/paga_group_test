from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import Account, Profile
from accounts.permissions import IsCreationOrIsAuthenticated, IsViewListOrIsAuthenticated
from accounts.serializers import AccountSerializer, ProfileSerializer


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsCreationOrIsAuthenticated,)

    def get_queryset(self):
        qs = super(AccountsViewSet, self).get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(pk=self.request.user.pk)
        return qs


class ProfilesListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsViewListOrIsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfilesRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super(ProfilesRetrieveUpdateView, self).get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(pk=self.request.user.pk)
        return qs
