# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.utils import timezone
# from decimal import Decimal
# from .models import OrderGrabbing, CustomUser
# from .serializers import  OrderGrabbingSerializer

# # class OrderViewSet(viewsets.ModelViewSet):
# #     queryset = Order.objects.all()
# #     serializer_class = OrderSerializer
# #     permission_classes = [AllowAny]

# class OrderGrabbingViewSet(viewsets.ModelViewSet):
#     queryset = OrderGrabbing.objects.all()
#     serializer_class = OrderGrabbingSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         user = request.user

#         original_balance = Decimal( user.balance) 
#         if user.level == "VIP1" and  user.balance > 0:
#             grab_amount = Decimal(100)
#             if user.balance < grab_amount - 1:
#                 return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

#             if user.grabbed_orders_count >= 3:
#                 return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)

#             user.balance = original_balance - grab_amount

#             # Calculate commission (20% of order price)

#             commission_amount = Decimal(20)  # Ensure commission_amount is a Decimal
#             today = timezone.now().date()  # Get today's date

#             # Check the last order grabbing day
#             last_grab_day = None
#             if user.ordergrabbing_set.exists():
#                 last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

#             # Update user's commission based on the day
#             if last_grab_day is None or last_grab_day == today:
#                 user.commission2 += commission_amount
#             else:
#                 user.commission1 += commission_amount
            
#             if  user.grabbed_orders_count == 0:
#                 user.unsettle = grab_amount + commission_amount
#             else:
#                 user.unsettle += grab_amount + commission_amount
            
#             # print(user.unsettle)
#             user.grabbed_orders_count + 1
#             user.save()


#             # Create order grabbing record
#             grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
           
#             serializer = self.get_serializer(grabbing)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         elif user.level == "VIP2" and  user.balance > 0:
#             grab_amount = Decimal(500)
#             if user.balance < grab_amount - 1:
#                 return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

#             if user.grabbed_orders_count >= 2:
#                 return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)
            
#             if user.grabbed_orders_count < 1:
#                 user.balance = original_balance - Decimal(1200) 
#             elif user.grabbed_orders_count >= 1:
#                 user.balance = original_balance - grab_amount
    
#             user.grabbed_orders_count + 1

#             # Calculate commission (20% of order price)

#             commission_amount = Decimal(12)  # Ensure commission_amount is a Decimal
#             today = timezone.now().date()  # Get today's date

#             # Check the last order grabbing day
#             last_grab_day = None
#             if user.ordergrabbing_set.exists():
#                 last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

#             # Update user's commission based on the day
#             if last_grab_day is None or last_grab_day == today:
#                 if user.grabbed_orders_count == 0:
#                     user.commission2 += Decimal(360)
#                 else:
#                     user.commission2 += Decimal(150)
#             else:
#                 if user.grabbed_orders_count == 0:
#                     user.commission1 += Decimal(360)
#                 else:
#                     user.commission1 += Decimal(150)
            
#             if  user.grabbed_orders_count == 0:
#                 user.unsettle = Decimal(1200) +  Decimal(360)
#                 # user.unsettle = Decimal(40) + commission_amount
#             else:
#                 user.unsettle += grab_amount +  Decimal(150)
#                 # user.unsettle += grab_amount +  Decimal((30/100) * 20)
#                 # user.unsettle += grab_amount + commission_amount

#             user.save()

#             # Create order grabbing record
#             grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
#             serializer = self.get_serializer(grabbing)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         elif user.level == "VIP3" and  user.balance > 0:
#             grab_amount = Decimal(2000)
#             commission_amount = Decimal(1000)  # Ensure commission_amount is a Decimal
#             if user.balance < grab_amount - 1:
#                 return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

#             if user.grabbed_orders_count >= 12:
#                 return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)

#             match user.grabbed_orders_count:
#                 case 0:
#                     user.balance = original_balance - Decimal(2000)
#                     user.unsettle = Decimal(2000) + commission_amount

#                 case 1:
#                     user.balance = original_balance - Decimal(4850)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(4850) + Decimal(2425)
#                 case 2:
#                     user.balance = original_balance - Decimal(7530)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(7530) + Decimal(3765)
#                 case 3:
#                     user.balance = original_balance - Decimal(12500)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(12500) + Decimal(6250)
#                 case 4:
#                     user.balance = original_balance - Decimal(20200)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(20200) + Decimal(10100)
#                 case 5:
#                     user.balance = original_balance - Decimal(12700)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(12700) + Decimal(6350)
#                 case 6:
#                     user.balance = original_balance - Decimal(35000)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(35000) + Decimal(17500)
#                 case 7:
#                     user.balance = original_balance - Decimal(37800)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(37800) + Decimal(18900)
#                 case 8:
#                     user.balance = original_balance - Decimal(55700)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(55700) + Decimal(27850)
#                 case 9:
#                     user.balance = original_balance - Decimal(43200)
#                     user.unsettle =Decimal(user.unsettle) +  Decimal(43200) + Decimal(21600)
#                 case 10:
#                     user.balance = original_balance - Decimal(63600)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(63600) + Decimal(31800)
#                 case 11:
#                     user.balance = original_balance - Decimal(85000)
#                     user.unsettle = Decimal(user.unsettle) + Decimal(85000) + Decimal(42500)
#                 case _:
#                     pass

#             # user.grabbed_orders_count += 1

#             # Calculate commission (20% of order price)
           
#             today = timezone.now().date()  # Get today's date

#             # Check the last order grabbing day
#             last_grab_day = None
#             if user.ordergrabbing_set.exists():
#                 last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

#             # Update user's commission based on the day
#             if last_grab_day is None or last_grab_day == today:
#                 user.commission2 += commission_amount
#             else:
#                 user.commission1 += commission_amount
#             user.save()

#             # Create order grabbing record
#             grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
#             serializer = self.get_serializer(grabbing)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
from decimal import Decimal
from .models import OrderGrabbing, CustomUser
from .serializers import  OrderGrabbingSerializer

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [AllowAny]

class OrderGrabbingViewSet(viewsets.ModelViewSet):
    queryset = OrderGrabbing.objects.all()
    serializer_class = OrderGrabbingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user

        original_balance = Decimal( user.balance) 
        if user.level == "VIP1" and  user.balance > 0:
            grab_amount = Decimal(100)
            if user.balance < grab_amount - 1:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

            if user.grabbed_orders_count >= 3:
                return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)

            user.balance = original_balance - grab_amount

            # Calculate commission (20% of order price)

            commission_amount = Decimal(20)  # Ensure commission_amount is a Decimal
            today = timezone.now().date()  # Get today's date

            # Check the last order grabbing day
            last_grab_day = None
            if user.ordergrabbing_set.exists():
                last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

            # Update user's commission based on the day
            if last_grab_day is None or last_grab_day == today:
                user.commission2 += commission_amount
            else:
                user.commission1 += commission_amount
            
            if  user.grabbed_orders_count == 0:
                user.unsettle = grab_amount + commission_amount
            else:
                user.unsettle += grab_amount + commission_amount
            
            # print(user.unsettle)
            user.grabbed_orders_count + 1
            user.save()


            # Create order grabbing record
            grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
           
            serializer = self.get_serializer(grabbing)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        elif user.level == "VIP2" and  user.balance > 0:
            grab_amount = Decimal(500)
            if user.balance < grab_amount - 1:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

            if user.grabbed_orders_count >= 2:
                return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)
            
            if user.grabbed_orders_count < 1:
                user.balance = original_balance - Decimal(1200) 
            elif user.grabbed_orders_count >= 1:
                user.balance = original_balance - grab_amount
    
            user.grabbed_orders_count + 1

            # Calculate commission (20% of order price)

            commission_amount = Decimal(12)  # Ensure commission_amount is a Decimal
            today = timezone.now().date()  # Get today's date

            # Check the last order grabbing day
            last_grab_day = None
            if user.ordergrabbing_set.exists():
                last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

            # Update user's commission based on the day
            if last_grab_day is None or last_grab_day == today:
                if user.grabbed_orders_count == 0:
                    user.commission2 += Decimal(360)
                else:
                    user.commission2 += Decimal(150)
            else:
                if user.grabbed_orders_count == 0:
                    user.commission1 += Decimal(360)
                else:
                    user.commission1 += Decimal(150)
            
            if  user.grabbed_orders_count == 0:
                user.unsettle = Decimal(1200) +  Decimal(360)
                # user.unsettle = Decimal(40) + commission_amount
            else:
                user.unsettle += grab_amount +  Decimal(150)
                # user.unsettle += grab_amount +  Decimal((30/100) * 20)
                # user.unsettle += grab_amount + commission_amount

            user.save()

            # Create order grabbing record
            grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
            serializer = self.get_serializer(grabbing)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        elif user.level == "VIP3" and  user.balance > 0:
            grab_amount = Decimal(2000)
            commission_amount = Decimal(1000)  # Ensure commission_amount is a Decimal
            if user.balance < grab_amount - 1:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

            if user.grabbed_orders_count >= 12:
                return Response({"error": "Grab limit reached"}, status=status.HTTP_400_BAD_REQUEST)

            if user.grabbed_orders_count == 0:
                user.balance = original_balance - Decimal(2000)
                user.unsettle = Decimal(2000) + commission_amount

            elif user.grabbed_orders_count == 1:
                user.balance = original_balance - Decimal(4850)
                user.unsettle = Decimal(user.unsettle) + Decimal(4850) + Decimal(2425)

            elif user.grabbed_orders_count == 2:
                user.balance = original_balance - Decimal(7530)
                user.unsettle = Decimal(user.unsettle) + Decimal(7530) + Decimal(3765)

            elif user.grabbed_orders_count == 3:
                user.balance = original_balance - Decimal(12500)
                user.unsettle = Decimal(user.unsettle) + Decimal(12500) + Decimal(6250)

            elif user.grabbed_orders_count == 4:
                user.balance = original_balance - Decimal(20200)
                user.unsettle = Decimal(user.unsettle) + Decimal(20200) + Decimal(10100)

            elif user.grabbed_orders_count == 5:
                user.balance = original_balance - Decimal(12700)
                user.unsettle = Decimal(user.unsettle) + Decimal(12700) + Decimal(6350)

            elif user.grabbed_orders_count == 6:
                user.balance = original_balance - Decimal(35000)
                user.unsettle = Decimal(user.unsettle) + Decimal(35000) + Decimal(17500)

            elif user.grabbed_orders_count == 7:
                user.balance = original_balance - Decimal(37800)
                user.unsettle = Decimal(user.unsettle) + Decimal(37800) + Decimal(18900)

            elif user.grabbed_orders_count == 8:
                user.balance = original_balance - Decimal(55700)
                user.unsettle = Decimal(user.unsettle) + Decimal(55700) + Decimal(27850)

            elif user.grabbed_orders_count == 9:
                user.balance = original_balance - Decimal(43200)
                user.unsettle = Decimal(user.unsettle) + Decimal(43200) + Decimal(21600)

            elif user.grabbed_orders_count == 10:
                user.balance = original_balance - Decimal(63600)
                user.unsettle = Decimal(user.unsettle) + Decimal(63600) + Decimal(31800)

            elif user.grabbed_orders_count == 11:
                user.balance = original_balance - Decimal(85000)
                user.unsettle = Decimal(user.unsettle) + Decimal(85000) + Decimal(42500)

            # user.grabbed_orders_count += 1

            # Calculate commission (20% of order price)
           
            today = timezone.now().date()  # Get today's date

            # Check the last order grabbing day
            last_grab_day = None
            if user.ordergrabbing_set.exists():
                last_grab_day = user.ordergrabbing_set.latest('grabbed_at').grabbed_at.date()

            # Update user's commission based on the day
            if last_grab_day is None or last_grab_day == today:
                user.commission2 += commission_amount
            else:
                user.commission1 += commission_amount
            user.save()

            # Create order grabbing record
            grabbing = OrderGrabbing.objects.create(user=user, commission=commission_amount, grabbed_at=timezone.now())
            serializer = self.get_serializer(grabbing)

            return Response(serializer.data, status=status.HTTP_201_CREATED)