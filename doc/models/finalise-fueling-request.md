
# Finalise Fueling Request

## Structure

`FinaliseFuelingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_name` | `str` | Optional | - |
| `timestamp` | `long\|int` | Optional | - |
| `volume_quantity` | `float` | Optional | - |
| `volume_unit` | `str` | Optional | - |
| `final_price` | `float` | Optional | - |
| `currency` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `site_address` | `str` | Optional | - |
| `original_price` | `float` | Optional | - |
| `discount` | `float` | Optional | - |
| `payment` | [`Payment`](../../doc/models/payment.md) | Optional | - |
| `products` | [`List[Product]`](../../doc/models/product.md) | Optional | - |
| `mpp_transaction_id` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "siteName": "Pentahof Site B 9997",
  "timestamp": 1548429960631,
  "volumeQuantity": 10.4,
  "volumeUnit": "LTR",
  "finalPrice": 23.3,
  "currency": "GBP",
  "status": "FINISHED",
  "siteAddress": "Test Geman Address",
  "originalPrice": 23.3,
  "discount": 0,
  "mppTransactionId": "000000006KCC"
}
```

