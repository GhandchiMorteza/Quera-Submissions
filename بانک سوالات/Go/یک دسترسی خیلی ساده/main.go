package main

type Permissions struct {
	canSeeMessages      bool
	canDeleteMessages   bool
	canEditMessages     bool
	canKickMembers      bool
	canMakeMembersAdmin bool
	canAddMembers       bool
}

func SetUserPermissions(permissions *Permissions) int8 {
	var num int8;
	bitIndices := []bool{
		permissions.canSeeMessages,
		permissions.canDeleteMessages,
		permissions.canEditMessages,
		permissions.canKickMembers,
		permissions.canMakeMembersAdmin,
		permissions.canAddMembers,
	}
	for idx, value := range bitIndices {
		if !value {
			continue
		}
		num |= 1 << idx
	}
	return num
}

func GetUserPermissions(permissionsMask int8) *Permissions {
	return &Permissions{		
		permissionsMask & (1 << 0) != 0,
		permissionsMask & (1 << 1) != 0,
		permissionsMask & (1 << 2) != 0,
		permissionsMask & (1 << 3) != 0,
		permissionsMask & (1 << 4) != 0,
		permissionsMask & (1 << 5) != 0,
	}
}
