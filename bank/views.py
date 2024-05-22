from rest_framework import generics
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankListView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchDetailView(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        branch_name = self.kwargs['branch_name']
        return Branch.objects.filter(name__icontains=branch_name)
