from rest_framework import serializers

from detransapp.models import TipoVeiculo


class TipoVeiculoSerializer(serializers.Serializer):
    codigo = serializers.IntegerField()
    descricao = serializers.CharField(max_length=40)
    # especies = EspecieSerializer(many=True, read_only=True)

    @staticmethod
    def restore_object(attrs, instance=None):
        if instance:
            instance.codigo = attrs.get('codigo', instance.codigo)
            instance.descricao = attrs.get('descricao', instance.descricao)
            # instance.especies = attrs.get('tipo_veiculo', instance.especies)

            return instance

        return TipoVeiculo(**attrs)
