from rest_framework import serializers
from .models import Expenses, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Expenses
        fields = ['id', 'description', 'amount', 'category', 'category_name', 'date']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context['request'].user
        return Expenses.objects.create(user=user, **validated_data)