from rest_framework import serializers

from accounts.models import Account, Profile


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('url', 'pk', 'email', 'password',)
        write_only = ('password',)
        read_only = ('pk',)

    def create(self, validated_data):
        user = Account(
            email=validated_data['email'],
            is_staff=False,
            is_active=True,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['pk', 'username', 'first_name', 'last_name', 'date_of_birth']
