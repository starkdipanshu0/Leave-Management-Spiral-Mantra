from django.db import models
from .manager import LeaveManager
from django.utils.translation import gettext as _
from django.utils import timezone
from datetime import datetime
from employee.models import CustomUser
from django.conf import settings
# Create your models here.

class Leave(models.Model):
	LEAVE_TYPE = (
		('casual', 'Casual Leave'),
		('paid', 'Paid Leave')
		)
	LEAVE_STATUS = {
		('approved', 'Approved'),
		('pending', 'Pending'),
		('cancelled', 'Cencelled'),
		('rejected', 'Rejected'),
	}
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
	startdate = models.DateField(verbose_name=_('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
	enddate = models.DateField(verbose_name=_('End Date'),help_text='coming back on ...',null=True,blank=False)
	leavetype = models.CharField(choices=LEAVE_TYPE,max_length=25,default='casual',null=True,blank=False)
	reason = models.CharField(verbose_name=_('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)

	status = models.CharField(choices=LEAVE_STATUS,max_length=10,default='pending',blank=False) #pending,approved,rejected,cancelled
	is_approved = models.BooleanField(default=False) #hide

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)


	objects = LeaveManager()


	class Meta:
		verbose_name = _('Leave')
		verbose_name_plural = _('Leaves')
		ordering = ['-created'] #recent objects



	def __str__(self):
		return ('{0} - {1}'.format(self.leavetype,self.user))


	@property
	def pretty_leave(self):
		'''
		i don't like the __str__ of leave object - this is a pretty one :-)
		'''
		leave = self.leavetype
		user = self.user
		employee = user.employee_set.first().get_full_name
		return ('{0} - {1}'.format(employee,leave))



	@property
	def leave_days(self):
		days_count = ''
		startdate = self.startdate
		enddate = self.enddate
		if startdate > enddate:
			return
		dates = (enddate - startdate)
		return dates.days



	@property
	def leave_approved(self):
		return self.is_approved == True




	def approve_leave(self):
		if not self.is_approved:
			self.is_approved = True
			self.status = 'approved'
			self.save()




	def unapprove_leave(self):
		if self.is_approved:
			self.is_approved = False
			self.status = 'pending'
			self.save()



	def leaves_cancel(self):
		if self.is_approved or not self.is_approved:
			self.is_approved = False
			self.status = 'cancelled'
			self.save()



	def reject_leave(self):
		if self.is_approved or not self.is_approved:
			self.is_approved = False
			self.status = 'rejected'
			self.save()

	@classmethod
	def leave_history(cls, user):
		return cls.objects.filter(user=user).order_by('-startdate')

	@property
	def is_rejected(self):
		return self.status == 'rejected'

