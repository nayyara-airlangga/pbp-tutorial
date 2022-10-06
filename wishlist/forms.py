from django import forms

from wishlist.models import BarangWishList


class CreateBarangWishlistForm(forms.ModelForm):
    class Meta:
        model = BarangWishList
        fields = ['nama_barang', 'harga_barang', 'deskripsi']

    nama_barang = forms.CharField(max_length=255)
    harga_barang = forms.IntegerField()
    deskripsi = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6, 'style': 'resize: none;'})
    )

    def save(self, user_id, commit=True):
        item = super().save(commit=False)

        if commit:
            item.save()

        return item
