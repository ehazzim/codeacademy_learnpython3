#Add weight of package
weight = 41.5

#Ground shipping
if weight <= 2:
  gs_cost = 20.00 + (weight * 1.50)
elif weight <= 6:
  gs_cost = 20.00 + (weight * 3.00)
elif weight <= 10:
  gs_cost = 20.00 + (weight * 4.00)
else:
  gs_cost = 20.00 + (weight * 4.75)

print(gs_cost)

#Ground Shipping Premium
gsp_cost = 125.00
print(gsp_cost)

#Drone Shipping
if weight <= 2:
  ds_cost = weight * 4.50
elif weight <= 6:
  ds_cost = weight * 9.00
elif weight <= 10:
  ds_cost = weight * 12.00
else:
  ds_cost = weight * 14.25

print(ds_cost)
